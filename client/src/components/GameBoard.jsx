import { useLoaderData } from "react-router-dom"
import { findLevel } from "../utils/loaders"
import { useEffect, useState } from "react"
import { shuffleEvents } from "../utils/actions/game_setup"

export default function GameBoard() {

  const loadedData = useLoaderData()

  const [ gameSetUp, setGameSetUp ] = useState()
  const [ gameState, setGameState ] = useState()
  const [ enemiesInDeck, setEnemiesInDeck ] = useState()
  const [ eventCards, setEventCards ] = useState()

  useEffect(() => {
    async function level() {
      console.log('loaded data ->', loadedData)
      const data = await findLevel(loadedData.mission)
      setGameState(data)
      console.log('data ->', data)
      setEnemiesInDeck(data.dark_legion_resources)
      const eventCardsData = await shuffleEvents(loadedData.mission, data.potential_events)
      setEventCards(eventCardsData)
    }
    level()
  }, [loadedData])
  

  

  return (
    <h2>Game Board</h2>
  )
}