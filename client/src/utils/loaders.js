import axios from 'axios'

export async function createGameLoader(){
  const res = await fetch(`/api/corporations/`)
  const corporations = await res.json()
  const res2 = await fetch(`/api/levels/`)
  const levels = await res2.json()
  return { corporations, levels }
}