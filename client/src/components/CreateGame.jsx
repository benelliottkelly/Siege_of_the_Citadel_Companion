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
  const navigate = useNavigate()

  // State
  const [ formData, setFormData ] = useState({
    owner: currentUser,
    campaign: '',
    mission: '',
    number_of_players: '',
    corporations: [],
    use_computer_to_draw_reinforcements: true
  })

  const [ res, setRes ] = useState(null)

  const { loggedIn, setLoggedIn } = useContext(loginContext)

  const [missionValue, setMissionValue] = useState(null);
  const [missionName, setMissionName] = useState('');
  const [errors, setErrors] = useState({});

  // Functions
  const handleSubmit = async (e) => {
    e.preventDefault()

    const newErrors = {};

    if (!formData.campaign) {
      newErrors.campaign = "Must select a campaign.";
    }

    if (!formData.mission) {
      newErrors.mission = "Must select a mission.";
    }

    if (!formData.number_of_players) {
      newErrors.number_of_players = "Number of players is required";
    }

    if (formData.number_of_players && formData.corporations.length != formData.number_of_players) {
      newErrors.corporations = `The number of corporations selected (${formData.corporations.length}) must be the same as the number of players (${formData.number_of_players})`;
    }

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return; // stop submit if there are errors
    }

    const state = {
      owner: currentUser,
      mission: missionValue,
      number_of_players: formData.number_of_players,
      corporations: formData.corporations,
      use_computer_to_draw_reinforcements: formData.use_computer_to_draw_reinforcements
    }

    sessionStorage.setItem("gameSetup", JSON.stringify(state))

    navigate("/games/board")
  }
  

  function handleChange(e) {
    // Remove error for specific field if it exists
    setErrors(({ [e.target.name]: _, ...errors }) => errors)

    // Set state for specific field
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  function handleArrayChange(e) {
    const fieldName = e.target.name
    // Remove error for specific field if it exists
    setErrors(({ [fieldName]: _, ...errors }) => errors)

    let arr = Array.from(e.target.selectedOptions, option => option.value)
    setFormData({ ...formData, [fieldName]: arr })
  }

  // Hooks
  useEffect(() => {
    if (formData.campaign && formData.mission) {
      // There are 5 missions in each campaign their PK is 1 - 10, the below matches the campaign and mission with their level
      let x = formData.campaign === "1" ? 0 : 5
      const missionPK = x + Number(formData.mission)
      setMissionValue(String(missionPK))
      setMissionName(levels.find(level => level["id"] === missionPK)["name"])
    }
  }, [formData.campaign, formData.mission]);

  return (
    <>
      <h2>Create Game</h2>
      <Form className='form' id='login-form' onSubmit={handleSubmit}>
        <div>
          <label>{missionName ? `Level Selected: ${missionName}` : "Level Select"}</label>
          <select value={formData.campaign} type="campaign" name="campaign" onChange={handleChange} placeholder='campaign'>
            <option value="" disabled>Campaign</option>
            {[1,2].map((i) => (<option value={i} label={i} key={uuidv4()}></option>))}
          </select>
          {errors.campaign && (<p className="formError">{errors.campaign}</p>)}
          <select value={formData.mission} type="mission" name="mission" onChange={handleChange} placeholder='mission'>
            <option value="" disabled>Mission</option>
            {[1,2,3,4,5].map((i) => (<option value={i} label={i} key={uuidv4()}></option>))}
          </select>
          {errors.mission && (<p className="formError">{errors.mission}</p>)}
        </div>
        <div>
          <label>Number of Players</label>
          <select value={formData.number_of_players} type="number_of_players" name="number_of_players" onChange={handleChange} placeholder="number_of_players">
            <option value="" disabled>Number of Players</option>
            {[1,2,3,4].map((i) => (<option value={i} label={i} key={uuidv4()}></option>))}
          </select>
          {errors.number_of_players && (<p className="formError">{errors.number_of_players}</p>)}
        </div>
        <div>
          <label>Corporations</label>
          <select value={formData.corporations} name="corporations" multiple onChange={handleArrayChange} disabled={!formData.number_of_players} style={{width:"80%"}}>
            <option label={formData.number_of_players ? `Select ${formData.number_of_players} ${formData.number_of_players > 1 ? "corporations" : "corporation"}` : "Chose the number of players before chosing corporations."} disabled/>
            {formData.number_of_players > 0 && corporations.length > 0 && corporations.map((corporation) => {
              return <option value={corporation.id} label={corporation.name} key={uuidv4()}></option>
            })}
          </select>
          {errors.corporations && (<p className="formError">{errors.corporations}</p>)}
        </div>
        <div>
          <label>Let Computer Draw Reinforcements<input checked={formData.use_computer_to_draw_reinforcements} type="checkbox" name="use_computer_to_draw_reinforcements" onChange={(e) => setFormData({...formData,use_computer_to_draw_reinforcements: e.target.checked,})}></input></label>
        </div>
        <button type="submit">Begin Mission</button>
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