export async function shuffleEvents(mission, event_cards){
  const mission_cards = []
  function addCardsToMission(rounds){
    // Take the number of event cards required for the mission from the full list of available event cards
    while (mission_cards.length < rounds) {
      let random = Math.floor(Math.random() * event_cards.length)
      console.log(`event cards length = ${event_cards.length}. random = ${random}`)
      let card_to_be_added = event_cards.splice(random, 1)
      console.log('card to be added ->', card_to_be_added)
      mission_cards.push(card_to_be_added)
    }
  }
  // missions with 5 rounds
  if (mission === 1 | mission === 2 | mission === 3 | mission === 7) {
    addCardsToMission(5)
  }
  // missions with 6 rounds
  else if (mission === 5) {
    addCardsToMission(6)
  }
  // missions with 7 rounds
  else if (mission === 4 | mission === 6 | mission === 8 | mission === 9) {
    addCardsToMission(7)
  }
  // missions with 10 rounds
  else if (mission === 10) {
    addCardsToMission(10)
  }
  console.log('mission cards ->', mission_cards)
  return mission_cards
}