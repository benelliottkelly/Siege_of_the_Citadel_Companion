import axios from 'axios'

export async function createGame(request){
  const data = await request
  return await axios.post('/api/games/', data, {
    validateStatus: () => true
  })
}