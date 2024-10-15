import { useState } from "react";
import emailjs from "@emailjs/browser";

const Contact = () => {

    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [message, setMessage] = useState("")

    const sendEmail = (e) => {
        if (name == "" || email == "" || message == "") {
            alert("Fill all of the e-mail fields")
            return;
        } else {
            e.preventDefault()
            const templateParams = {
                from_name: name,
                email: email,
                message: message
            }
            emailjs.send("service_95t6kff", "template_b52uxes", templateParams, "YiJDkWIzUG8xLPs37")
                .then((res) => {
                    console.log("E-mail sent", res.status,)
                    setName(""),
                        setEmail(""),
                        setMessage("")
                }, (error) => {
                    console.log("Error:", error)
                })
        }
    }

    return (
        <section className="email" style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
        }}>
            <form onSubmit={sendEmail}>
                <input
                    className="input"
                    type="text"
                    placeholder="Your name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
                <input
                    className="input"
                    type="text"
                    placeholder="Your e-mail"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <textarea
                    style={{
                        verticalAlign: 'middle',
                        resize: 'both',
                        height: '2rem',
                        maxWidth: '600px',
                        minWidth: '200px',
                        maxHeight: '200px',
                        minHeight: '50px',
                    }}
                    className="text"
                    type="text"
                    placeholder="Your message"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                />
                <button type="submit" className="btn">Send</button>
            </form>
        </section>
    )
}

export default Contact;