import { Link } from 'react-router-dom'
import { removeToken } from '../utils/helpers/common'

export default function Nav() {

  //Functions
  function handleLogOut(){
    console.log('clicked')
    removeToken()
  }

  return (
    <header>
      <nav>
        <Link className='nav-link' to={'/'}><button>Home</button></Link>
        <Link className='nav-link' to={'/login/'}><button>Login</button></Link>
        <Link className='nav-link' to={'/register/'}><button>Register</button></Link>
        <button onClick={handleLogOut}>Logout</button>
      </nav>
    </header>
  )
}