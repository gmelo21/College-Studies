import Entry from "./components/Entry"
import Info from "./components/Info"
import Data from "./components/Data"
import Counter from "./components/Counter"

function App() {

  return (
    <>
      <Entry/>

      <Info name="Messmer, the Impaler" email="twinsnakes@gmail.com" />

      <Data level="Demigod" name="Marika, Radagon" password="The Golden Order" />

      <Counter/>
    </>
  )
}

export default App
