import Nav from "./Nav"
import { Link } from "react-router-dom"

export default function Home() {

  return (
    <>
      <div className="hero" style={{background:"url('./src/assets/misc/box-art-zoomed.jpg') no-repeat top center", backgroundSize: "cover", height:"90vh", display: "flex", flexDirection: "column", justifyContent:"center", alignItems: "center"}}>
        <div style={{display: "flex", flexDirection: "column", justifyContent:"center", alignItems: "center", width: "100%"}}>
          <img src="./src/assets/misc/siege-of-the-citadel-logo.png" alt="Siege of the Citadel logo" style={{width:"50%"}}/>
          <h1 style={{margin: "0px 0px 0.5em", color: "black", textShadow: "-1px -1px 0 #69a37e80, 1px -1px 0 #69a37e80, -1px 1px 0 #69a37e80, 1px 1px 0 #69a37e80"}}>Companion App</h1>
          <Link to={'/games/create/'}><button>Create New Game</button></Link>
        </div>
      </div>
    </>
  )
}