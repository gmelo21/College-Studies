import "./home.css";

const Home = () => {
  return (
    <>
      <div className="jumbotron">
        <h1 className="display-4">Hello, GitHub!</h1>
        <p className="lead">
          This is a jumbotron, used to call your attention and also has a cool
          Transformers name.
        </p>
        <hr className="my-4" />
        <p>
          It uses utility classes for typography and spacing to space content
          out within the larger container, taken directly from our new friend,
          bootstrap!
        </p>
        <a className="btn btn-primary btn-lg" href="#told-you" role="button">
          Nothing will happen if you click here.
        </a>
      </div>
    </>
  );
};

export default Home;
