import { Outlet } from 'react-router-dom'
import Side from './components/Side/Side'

function App() {
  return (
    <>
      <Side />
      <Outlet />
    </>
  )
}

export default App