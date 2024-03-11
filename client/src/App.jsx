import { Outlet } from 'react-router-dom'
import { LoginProvider } from './components/LoginContext'

function App() {
  

  return (
    <>
      <LoginProvider>
        <Outlet />
      </LoginProvider>
    </>
  )
}

export default App
