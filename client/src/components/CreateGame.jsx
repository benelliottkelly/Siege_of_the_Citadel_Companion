import { useEffect, useState, useContext } from 'react'
import { Form, useNavigate, Link, useLoaderData } from 'react-router-dom'
import { loginContext } from './LoginContext'
import { getUser } from "../utils/helpers/common"
import { createGame } from '../utils/actions/create'
import { v4 as uuidv4 } from 'uuid'
import Nav from "./Nav"

export default function CreateGame() {

  const currentUser = getUser()
  const loadedData = useLoaderData()
  const { corporations, levels } = loadedData
  console.log(loadedData)
  const navigate = useNavigate()

  // State
  const [ formData, setFormData ] = useState({
    owner: currentUser,
    mission: '',
    number_of_players: '',
    corporations: [],
    use_computer_to_draw_reinforcements: ''
  })

  const [ res, setRes ] = useState(null)

  const { loggedIn, setLoggedIn } = useContext(loginContext)

  // Functions
  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const response = await createGame(formData)
      setRes(response)
    } catch (error) {
      console.log(error)
    }
  }

  function handleChange(e) {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  function handleArrayChange(e) {
    let arr = []
    e.forEach((item) => {
      arr.push(item.value)
    })
    setFormData({ ...formData, genre: arr })
  }

  return (
    <>
      <Nav />
      <h2>Create Game</h2>
      <Form className='form' id='login-form' onSubmit={handleSubmit}>
        <input type="mission" name="mission" onChange={handleChange} placeholder='mission' />
        <input type="number_of_players" name="number_of_players" onChange={handleChange} placeholder="number_of_players" />
        <select multiple onChange={handleArrayChange}>
          {corporations.length > 0 && corporations.map((corporation) => {
            return <option value={corporation.id} label={corporation.name} key={uuidv4()}></option>
          })}
        </select>
        <button type="submit">Login</button>
        {res && 
          <div>
            <button onClick={resetRes}>❌</button>
            <p>{res.status}: {res.statusText}</p>
          </div>
        }
      </Form>
    </>
  )
}