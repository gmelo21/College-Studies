import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import {createBrowserRouter,RouterProvider} from 'react-router-dom'
import App from './App.jsx'
import Error from './routes/Error.jsx'
import Home from './routes/Home.jsx'
import Aluno from './routes/Aluno.jsx'


const router= createBrowserRouter([
{
  path:'/', element:<App/>,
  errorElement:<Error/>,

  children:[
    {path:'/', element:<Home/>},
    {path:'/aluno', element:<Aluno/>},
  ]
}
])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    {/*Text line*/}
    <RouterProvider router={router} />
  </StrictMode>,
)