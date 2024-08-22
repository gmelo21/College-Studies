const Button=()=>{
    const handleClick=()=>{
        alert("You clicked in a button component.")
    }

    return(
        <>
        <button onClick={handleClick}>Click here</button>
        </>
    )
}

export default Button