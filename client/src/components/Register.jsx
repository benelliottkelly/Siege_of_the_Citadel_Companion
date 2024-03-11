import Nav from "./Nav"
import { useEffect, useState } from 'react'
import { Form, useActionData, useNavigate, Link } from 'react-router-dom'
import ImageUploadField from "./ImageUploadField"
import { registerUser } from "../utils/actions/auth"

export default function Register() {

  // States
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    username: '',
    email: '',
    password: '',
    password_confirmation: '',
    image: null
  })

  const [ res, setRes ] = useState(null)

  // Functions
  function handleChange(e) {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const response = await registerUser(formData)
      setRes(response)
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    if (res?.status === 200) {
      navigate(`/login/`)
    }
  }, [res])

  // Clears the register error message
  function resetRes(){
    setRes(null)
  }

  return (
    <>
      <Nav />
      <section className="form-container">
        <h1>Register</h1>
        <Form className='form' id='register-form' onSubmit={handleSubmit} method="POST">
          <input type="text" name="username" placeholder='Username' required onChange={handleChange} value={formData.username} />
          <input type="email" name="email" placeholder='email' required onChange={handleChange} value={formData.email} />
          <input type="text" name="first_name" placeholder='First Name' onChange={handleChange} value={formData.first_name} />
          <input type="text" name="last_name" placeholder='Last Name' onChange={handleChange} value={formData.last_name} />
          <input type="password" name="password" placeholder='Password' required onChange={handleChange} value={formData.password} />
          <input type="password" name="password_confirmation" placeholder='Password Confirmation' required onChange={handleChange} value={formData.password_confirmation} />
          <ImageUploadField setFormData={setFormData} formData={formData} /> {/* This line needs to change the hidden line below */}
          <input type='hidden' name='image' value={formData.image ? formData.image : 'insert default image link here'} />
          <button type="submit">Register</button>
          {res && 
            <div>
              <button onClick={resetRes}>❌</button>
              <p>{res.status}: {Object.values(res.data)[0]}</p>
            </div>
          }
          <p>Already registered? Click to <Link to={'/login'}>Login</Link> instead.</p>
        </Form>
      </section>
    </>
  )
}