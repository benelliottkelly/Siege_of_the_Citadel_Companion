import { Outlet } from 'react-router-dom'
import { LoginProvider } from './components/LoginContext'
import Nav from './components/Nav'

function App() {
  

  return (
    <>
      <LoginProvider>
        <Nav />
        <Outlet />
      </LoginProvider>
    </>
  )
}

export default App
