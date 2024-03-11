import { Link } from 'react-router-dom'

export default function Nav() {
  return (
    <header>
      <nav>
        <Link className='nav-link' to={'/'}><button>Home</button></Link>
        <Link className='nav-link' to={'/login/'}><button>Login</button></Link>
        <Link className='nav-link' to={'/register/'}><button>Register</button></Link>
      </nav>
    </header>
  )
}