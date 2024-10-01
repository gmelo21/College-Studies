import {Data} from "../components/Data"

const Student=()=>{
    const {name, email, age} = Data

    return(
        <>
        <h1>Normal student's page.</h1>
        <p>Student name: {name}</p>
        <p>Student's e-mail: {email}</p>
        <p>Student's age: {age}</p>
        <h6>Hey, chump. Add a little "/(whatever)" to the end of the search bar. It's a cool secret.</h6>
        </>

    )

}

export default Student