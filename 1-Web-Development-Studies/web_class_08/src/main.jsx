import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import App from './App.jsx'
import Home from './routes/Home/Home.jsx'
import Error from './routes/Error/Error.jsx'
import Page1 from './routes/Pages/Page1.jsx'
import Page2 from './routes/Pages/Page2.jsx'
import Page3 from './routes/Pages/Page3.jsx'

const router = createBrowserRouter([{
  path: '/', element: <App />,
  errorElement: <Error />,

  children: [
    { path: '/', element: <Home /> },
    { path: '/page1', element: <Page1 /> },
    { path: '/page2', element: <Page2 /> },
    { path: '/page3', element: <Page3 /> },
  ]

}])

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
)
