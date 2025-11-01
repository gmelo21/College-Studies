import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import "./about.css";
import { Container } from "react-bootstrap";

const About = () => {
  return (
    <>
      <Container className="container">
        <Card style={{ width: "18rem" }}>
          <Card.Img variant="top" src="holder.js/100px180" />
          <Card.Body>
            <Card.Title>Card Title</Card.Title>
            <Card.Text>
              Imagine there is some cool, life-changing, inspiring text here. Like the ones in LinkedIn.
            </Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
        </Card>

        <Card style={{ width: "18rem" }}>
          <Card.Img variant="top" src="holder.js/100px180" />
          <Card.Body>
            <Card.Title>Card Title</Card.Title>
            <Card.Text>
              Imagine there is some cool, life-changing, inspiring text here. Like the ones in LinkedIn.
            </Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
        </Card>

        <Card style={{ width: "18rem" }}>
          <Card.Img variant="top" src="holder.js/100px180" />
          <Card.Body>
            <Card.Title>Card Title</Card.Title>
            <Card.Text>
              Imagine there is some cool, life-changing, inspiring text here. Like the ones in LinkedIn.
            </Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
        </Card>
      </Container>
    </>
  );
};

export default About;
