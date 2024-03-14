import Nav from "./Nav"
import { Link } from "react-router-dom"

export default function Home() {

  return (
    <>
      <Nav />
      <h1>Siege of the Citadel Companion</h1>
      <Link to={'#'}><button>Profile</button></Link>
      <Link to={'/games/create/'}><button>Create New Game</button></Link>
    </>
  )
}