import { useEffect, useState, useContext } from 'react'
import { Form, useNavigate, Link, useLoaderData } from 'react-router-dom'
import { loginContext } from './LoginContext'
import { getUser } from "../utils/helpers/common"
import { createGame } from '../utils/actions/create'
import Select from 'react-select'
import { v4 as uuidv4 } from 'uuid'
import Nav from "./Nav"

export default function CreateGame() {
  const loadedData = useLoaderData()
  const { corporations, levels } = loadedData
  const navigate = useNavigate()

  // State
  const [ formData, setFormData ] = useState({
    owner: '',
    mission: '',
    number_of_players: '',
    corporations: [],
    use_computer_to_draw_reinforcements: true
  })

  const [ levelSelect, setLevelSelect ] = useState({
    campaign: '',
    mission: ''
  })

  const [ owner, setOwner ] = useState('')

  const [ res, setRes ] = useState(null)

  const { loggedIn, setLoggedIn } = useContext(loginContext)

  const [isChecked, setIsChecked] = useState(true);

  // Functions
  const handleSubmit = async (e) => {
    e.preventDefault()
    if (parseInt(formData['number_of_players']) === formData['corporations'].length){
      try {
        const response = await createGame(formData)
        setRes(response)
      } catch (error) {
        console.log(error)
      }
    } else {
      setRes({
        status: 400,
        data: ['Number of players should match the number of corporations selected.']
      })
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

  useEffect(() => {
    const currentUser = getUser()
    setOwner(currentUser)
  }, [])

  useEffect(() => {
    setFormData({ ...formData, owner: owner })
  }, [owner])

  useEffect(() => {
    if (parseInt(levelSelect['campaign']) === 1 && (parseInt(levelSelect['mission']) > 0 && parseInt(levelSelect['mission']) <= 5)) {
      setFormData({ ...formData, mission: parseInt(levelSelect['mission']) })
    } else if (parseInt(levelSelect['campaign']) === 2 && (parseInt(levelSelect['mission']) > 0 && parseInt(levelSelect['mission']) <= 5)) {
      setFormData({ ...formData, mission: parseInt(levelSelect['mission']) + 5 })
    }
  }, [levelSelect])

  useEffect(() => {
    if (res?.status === 201) {
      navigate(`/games/${res.data.id}`)
    }
    console.log(res)
  }, [res])

  useEffect(() => {
    setFormData({ ...formData, use_computer_to_draw_reinforcements: isChecked })
  }, [isChecked])
  // Clears the register error message
  function resetRes(){
    setRes(null)
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
          name='corporations'
          placeholder='Corportations'
          onChange={handleReactSelectChange}
          options={corporations.length > 0 && corporations.map((corporation) => {
            return {value: corporation.id, label: corporation.name, key: uuidv4()}
          })}
        />
        <label><input type="checkbox" checked={isChecked} name='use_computer_to_draw_reinforcements' value={isChecked} onChange={() => setIsChecked((prev) => !prev)}/> Use Computer to Generate Reinforcements</label>
        <button type='submit'>Create Game</button>
        {res >= 400 && 
          <div>
            <button onClick={resetRes}>❌</button>
            <p>{res.status}: {Object.values(res.data)[0]}</p>
          </div>
        }
      </Form>
    </>
  )
}