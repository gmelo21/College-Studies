import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import {createBrowserRouter,RouterProvider} from 'react-router-dom'
import App from './App.jsx'
import Error from './routes/Error.jsx'
import Home from './routes/Home.jsx'
import Student from './routes/Student.jsx'


const router = createBrowserRouter([{
  path: '/', element: <App/>,
  errorElement: <Error/>,

  children:[
    {path: '/', element: <Home/>},
    {path: '/student', element: <Student/>},

  ]

}])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    {/*Text line example!*/}
    <RouterProvider router={router} />
    
  </StrictMode>,

)