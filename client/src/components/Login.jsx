import { useEffect, useState, useContext } from 'react'
import { Form, useNavigate, Link } from 'react-router-dom'
import { loginUser } from '../utils/actions/auth'
import { setToken } from '../utils/helpers/common'
import { loginContext } from './LoginContext'

import Nav from './Nav'

export default function Login() {

  const navigate = useNavigate()

  // State
  const [ formData, setFormData ] = useState({
    username: '',
    password: ''
  })

  const [ res, setRes ] = useState(null)

  const { loggedIn, setLoggedIn } = useContext(loginContext)

  // Functions
  function handleChange(e) {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const response = await loginUser(formData)
      console.log(response)
      setRes(response)
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    // If login is successful...
    if (res?.status === 200) {
      // set the access token to local stor
      setToken(res.data.access)
      // set the logged in context to true
      setLoggedIn(true)
      // navigate back to the homepage
      navigate('/')
    }
  }, [res])

  // Clears the login error message
  function resetRes(){
    setRes(null)
  }

  return (
    <>
      <Nav />
      <h2>Login</h2>
      <Form className='form' id='login-form' onSubmit={handleSubmit}>
          <input type="username" name="username" onChange={handleChange} placeholder='Username' />
          <input type="password" name="password" onChange={handleChange} placeholder="Password" />
          <button type="submit">Login</button>
          {res && 
            <div>
              <button onClick={resetRes}>❌</button>
              <p>{res.status}: {res.statusText}</p>
            </div>
          }
      </Form>
      <p>Don't have an account? Please <Link to={'/register/'}>register here</Link>.</p>
    </>
  )
}