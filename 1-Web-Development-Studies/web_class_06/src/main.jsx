import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Error from './routes/Error/Error.jsx'
import App from './App.jsx'
import Home from './routes/Home/Home.jsx'

const router = createBrowserRouter([{
  path: '/', element: <App />,
  errorElement: <Error />,

  children: [{
    path: '/',
    element: <Home />,
  }]
}])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)