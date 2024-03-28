import { useEffect, useState, useContext } from 'react'
import { Form, useNavigate, Link, useLoaderData } from 'react-router-dom'
import { loginContext } from './LoginContext'
import { getUser } from "../utils/helpers/common"
import { createGame } from '../utils/actions/create'
import Select from 'react-select'
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

  const [ levelSelect, setLevelSelect ] = useState({
    campaign: '',
    mission: ''
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

  function handleReactSelectChange(e) {
    let arr = []
    e.forEach((item) => {
      arr.push(item.value)
    })
    setFormData({ ...formData, corporations: arr })
  }

  function handleLevelSelectChange(e) {
    setLevelSelect({ ...levelSelect, [e.target.name]: e.target.value })
  }

  return (
    <>
      <Nav />
      <h2>Create Game</h2>
      <Form className='form' id='login-form' onSubmit={handleSubmit}>
        <select name='campaign' onChange={handleLevelSelectChange} placeholder='campaign'>
          <option selected disabled>Campaign</option>
          <option value={1}>1</option>
          <option value={2}>2</option>
        </select>
        <select name='mission' onChange={handleLevelSelectChange} placeholder='mission'>
          <option selected disabled>Mission</option>
          <option value={1}>1</option>
          <option value={2}>2</option>
          <option value={3}>3</option>
          <option value={4}>4</option>
          <option value={5}>5</option>
        </select>
        <select name='number_of_players' onChange={handleChange} placeholder='Number of Players'>
          <option selected disabled>Number of Players</option>
          <option value={1}>1</option>
          <option value={2}>2</option>
          <option value={3}>3</option>
          <option value={4}>4</option>
        </select>
        <Select
          defaultValue={[]}
          isMulti
          name="genre"
          onChange={handleReactSelectChange}
          options={corporations.length > 0 && corporations.map((corporation) => {
            return {value: corporation.id, label: corporation.name, key: uuidv4()}
          })}
        />
        <button type='submit'>Login</button>
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