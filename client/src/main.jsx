import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

// Styles
import './styles/main.scss'

// Components
import Home from './components/Home.jsx'
import Register from './components/Register.jsx'
import Login from './components/Login.jsx'
import Games from './components/Games.jsx'
import CreateGame from './components/CreateGame.jsx'
import GameBoard from './components/GameBoard.jsx'

// Loaders
import { createGameLoader } from './utils/loaders.js'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        path: '/',
        element: <Home />,
      },
      {
        path: '/register',
        element: <Register />,
      },
      {
        path: '/login',
        element: <Login />,
      },
      {
        path: '/games',
        element: <Games />,
      },
      {
        path: '/games/create',
        element: <CreateGame />,
        loader: createGameLoader
      },
      {
        path: '/games/:gamepk',
        element: <GameBoard />,
      }
    ],
  },
])

ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router} />
)
