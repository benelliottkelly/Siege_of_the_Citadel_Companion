import Nav from "./Nav"
import { useEffect, useState } from 'react'
import { Form, useActionData, useNavigate, Link } from 'react-router-dom'

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

  function handleChange(e) {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  return (
    <>
      <Nav />
      <section className="form-container">
        <h1>Register</h1>
        <Form className='form' id='register-form' method='POST'>
          <input type="text" name="first_name" placeholder='First Name' onChange={handleChange} value={formData.username} />
          <input type="text" name="last_name" placeholder='Last Name' required onChange={handleChange} value={formData.username} />
          <input type="text" name="username" placeholder='Username' required onChange={handleChange} value={formData.username} />
          <input type="email" name="email" placeholder='email' required onChange={handleChange} value={formData.email} />
          <input type="password" name="password" placeholder='New Password' required onChange={handleChange} value={formData.password} />
          <input type="password" name="password_confirmation" placeholder='Password Confirmation' required onChange={handleChange} value={formData.password_confirmation} />
          {/* <ImageUploadField setFormData={setFormData} formData={formData} /> This line needs to change the hidden line below */}
          {/* <input type='hidden' name='image' value={formData.image ? formData.image : 'insert default image link here'} /> */}
          <button className='btn form-button' type="submit">Register</button>
          {/* {res && <p className='danger'>{res.status}: {res.statusText}</p>} */}
          <p>Already registered? Click to <Link to={'/login'}>Login</Link> instead.</p>
        </Form>
      </section>
    </>
  )
}