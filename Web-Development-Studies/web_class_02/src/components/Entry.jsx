import Button from "./Button"

const Entry=()=>{
    let name="my GitHub";

    function click(){
        alert(`You're at ${name}!`)

    }

    return(
    <>
    <p>Hello, world!</p>
    <p>Welcome back to {name}.</p>
    <button onClick={click}>Click here</button>
    <h3>Button component down here:</h3>
    <Button/>
    </>

    )
    
}

export default Entry