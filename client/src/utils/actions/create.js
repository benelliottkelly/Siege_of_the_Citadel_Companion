import axios from 'axios'
import { getToken } from '../helpers/common'

export async function createGame(request){
  const data = await request
  return await axios.post('/api/games/', data, {
    validateStatus: () => true,
    headers: {
      Authorization: `Bearer ${getToken()}`
    }
  })
}