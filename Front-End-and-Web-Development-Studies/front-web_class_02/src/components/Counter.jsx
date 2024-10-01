import {useState} from 'react'

const Counter=()=>{
    const [counter,setCounter]=useState(0);

    return(
        <>
        <p>Death counter: {counter}</p>
        <button onClick={()=>setCounter(counter +1)}>Increase</button>
        <button onClick={()=>setCounter(counter -1)}>Decrease</button>
        </>

    )
    
}

export default Counter