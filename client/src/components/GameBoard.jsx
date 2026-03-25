// import { useLocation } from "react-router-dom"
import { useNavigate } from "react-router-dom"
import Map from "./Map"
import { useState, useEffect } from "react"
import { maps } from "../utils/data/maps"

export default function GameBoard() {

  const navigate = useNavigate()
  // const { state } = useLocation()
  const [ gameSetup, setGameSetup ] = useState(null)
  const [ sessionErrorMessage, setSessionErrorMessage ] = useState(null)
  const [ levelDetails, setLevelDetails ] = useState(null)
  const [ turnsRemaining, setTurnsRemaining ] = useState(null)
  const [ finalRound, setFinalRound ] = useState(false)
  const [ tiles, setTiles ] = useState(null)


  const [ events, setEvents ] = useState(null)
  const [ darkLegion, setDarkLegion ] = useState(null)

  const { owner, mission, number_of_players: numberOfPlayers, corporations, use_computer_to_draw_reinforcements: drawReinforcements } = gameSetup || {}
  const { campaign, mission: levelNumber, name, map_tiles: mapTiles, dark_legion_entrance_points: darkLegionEntrancePoints, additional_setup: additionalSetup, time_limit: timeLimit, potential_events: potentialEvents, dark_legion_resources: darkLegionResources } = levelDetails || {}

  const EVENTS_WITH_SPECIAL_RULES = [15, 16, 17, 20, 21, 22, 23, 24]


  useEffect(() => {
    let timeoutId;

    try {
      const storedGameSetup = sessionStorage.getItem("gameSetup");

      if (!storedGameSetup) {
        throw new Error("Missing gameSetup session storage.");
      }

      const parsed = JSON.parse(storedGameSetup);
      console.log("parsed:")
      console.log(parsed)
      setGameSetup(parsed);
    } catch {
      setSessionErrorMessage(
        "Could not find game setup state. Redirecting to game creation screen..."
      );

      timeoutId = setTimeout(() => {
        navigate("/games/create");
      }, 3000);
    }

    return () => {
      if (timeoutId) clearTimeout(timeoutId);
    };
  }, [navigate]);

  // Set the useStates from levels API call
  useEffect(() => {
        async function fetchLevel() {
            const res = await fetch(`/api/levels/${mission}`)
            const json = await res.json()
            console.log(json)
            setLevelDetails(json)


            setTurnsRemaining(json.time_limit)
        }
        
        if (mission) {
          fetchLevel()
        }
    }, [gameSetup])
  
  useEffect(() => {
    if ( levelDetails ) {
          const events = getEvents(potentialEvents, timeLimit)
          setEvents({
            undrawnCards: [... events],
            currentCard: [],
            discardedCards: []
          })
          console.log(events)
          const darkLegionCards = structuredClone(darkLegionResources)
          const tiles = structuredClone(mapTiles)

          addReinforcementsToTiles(darkLegionCards, tiles)

          // ToDo Add custom logic for level 4 and 5s setup

          // Adds a reinforment card for each player to the required tiles according to the level setup
          setTiles(tiles)

          // Adds the remaining cards to the draw pile
          setDarkLegion({
            undrawnCards: darkLegionCards,
            currentCards: [],
            discardedCards: [],
            removedCards: []
            })
          
        }
  }, [levelDetails])

  // ToDo If I want to remove the session storage at any point can call this function
  function closeGame() {
    sessionStorage.removeItem("gameState");
  }

  function getEvents(availableEvents, timer) {
    if (timer > availableEvents.length) {
      throw new Error("x cannot be larger than array length")
    }

    const shuffled = [...availableEvents] // copy to avoid mutating original

    for (let i = shuffled.length - 1; i > 0; i--) {
      const n = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[n]] = [shuffled[n], shuffled[i]]
    }

    return shuffled.slice(0, timer)
  }

  function getNextEvent() {
    let events_copy = structuredClone(events)

    if ( events_copy["currentCard"].length > 0 ) {
      events_copy["discardedCards"].push(events_copy["currentCard"][0])
      events_copy["currentCard"] = []
    }
    const n = Math.floor(Math.random() * (events_copy["undrawnCards"].length))
    events_copy["currentCard"].push(events_copy["undrawnCards"][n])

    events_copy["undrawnCards"].splice(n, 1)
    const cards_left = events_copy["undrawnCards"].length
    if ( cards_left === 0) {
      setFinalRound(true)
      console.log("Final round")
    }
    setTurnsRemaining(cards_left)
    setEvents(events_copy)

    drawDarkLegionFromEvents(events_copy["currentCard"][0]["number"])
    
  }

  function drawDarkLegionFromEvents(eventNumber){
    const darkLegionClone = structuredClone(darkLegion)

    let {
      undrawnCards,
      currentCards,
      discardedCards,
      removedCards,
    } = darkLegionClone

    if (!EVENTS_WITH_SPECIAL_RULES.includes(eventNumber)) {

      // ToDo Add logic for "special events"

      // 15 - Reinforcements = 1 Centurion, 1 Necromutant, 2 Legionnaires per Corporation player

      // 16 - Reinforcements = 1 Centurion, Draw as many force cards as there are Corporation players

      // 17 - Reinforcements = 1 Razide, Draw as many force cards as there are Corporation players

      // 20 -  Reinforcements = 2 Praetorian Stalkers

      // 21 - Reinforcements = 1 Nepharite, 1 Necromutant, 1 Legionnaire

      // 22 - Reinforcements = 1 Ezoghoul, 3 Legionnaires

      // 23 - Reinforcements = 1 Legionnaire, Draw as many force cards as there are Corporation players

      // 24 - Reinforcements = 1 Razide, Draw as many force cards as there are Corporation players 

      let addCardToCurrentCards = true
      let x = 0
      while (addCardToCurrentCards) {
        // If the draw pile is empty, add the discarded cards back into the draw pile
        if (!undrawnCards.length) {
          console.log("Draw pile empty, reshuffling discard into draw.")
          undrawnCards.push(...discardedCards)
          discardedCards.length = 0
        }

        // Randomise the card that is about to be drawn
        const n = Math.floor(Math.random() * (undrawnCards.length))
        console.log(`Adding card ${undrawnCards[n]["name"]}`)
        // Check if the card that is being drawn has a stop drawing prompt
        if (undrawnCards[n]["stop_drawing"]) {
          console.log("Card has stop drawing prompt.")
          addCardToCurrentCards = false
        }
        x += 1
        // Check if the number of cards drawn is >= the number of players and that card being drawn doesn't have the draw another card prompt
        if ( x >= numberOfPlayers && !undrawnCards[n]["draw_one_more"]) {
          console.log("End of event draw")
          addCardToCurrentCards = false
        }
        // Removes the drawn card from the undrawn cards and adds it to current cards array
        currentCards.push(undrawnCards.splice(n, 1)[0])
      }
    }

    setDarkLegion(
      {
        undrawnCards: undrawnCards,
        currentCards: currentCards,
        discardedCards: discardedCards,
        removedCards: removedCards
      }
    )    
    
  }

  function addReinforcementsToTiles(darkLegionCards, tiles) {
    for (let i = 0; i < tiles["tiles"].length; i++ ) {
      console.log(tiles["tiles"][i])
      if (tiles["tiles"][i]["force_cards"]) {
        corporations.forEach(_ => {
          const n = Math.floor(Math.random() * (darkLegionCards.length))
          tiles["tiles"][i]["cards_on_tile"].push(darkLegionCards.splice(n, 1)[0])
        })
      }
    }
  }

  const handleTileClick = (tile ) => {
    console.log(tile)
  }

  return (
    <>
      <h2>Game Board</h2>
      {sessionErrorMessage ?
        <div>
          <h3>{sessionErrorMessage}</h3>
        </div>
        : levelDetails &&
        <div style={{display:"flex", flexFlow:"column nowrap"}}>
          {(turnsRemaining || turnsRemaining === 0) && (
            <div>
              <h3>Turns Remaining:</h3>
              <h3>{turnsRemaining}</h3>
            </div>
          )}
          {tiles && <Map level={mission} mapTiles={tiles} onTileClick={handleTileClick}/>}
          {!finalRound &&
          <button onClick={getNextEvent}>Start Dark Legions Turn</button>
          }
          {(events?.currentCard?.[0]) && (
            <button>Show Current Event</button>
          )}
        </div>
      }
    </>
  )
}