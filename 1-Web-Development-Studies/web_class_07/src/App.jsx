import { Outlet } from "react-router-dom";
import Nav from "./components/Nav/Nav";
import Footer from "./components/Footer/Footer";
import "./app.css";

function App() {
  return (
    <>
      <div id="container-page">
        <div id="header-page">
          <Nav />
        </div>
        <div id="main-page">
          <Outlet id="outlet-page" />
        </div>
        <div id="footer-page">
          <Footer />
        </div>
      </div>
    </>
  );
}

export default App;
