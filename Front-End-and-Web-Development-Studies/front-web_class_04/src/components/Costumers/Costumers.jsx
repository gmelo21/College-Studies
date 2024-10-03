import { useForm } from "react-hook-form";

const Costumers = () => {

    const { register, handleSubmit, setValue, setFocus } = useForm({});

    const findCep = (e) => {
        const cep = e.target.value;
        fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then((res) => res.json())
            .then((dados) => {
                setValue("street", dados.logradouro);
                setValue("city", dados.localidade);
                setFocus("number");
            })
    }

    return (
        <>
            <section className="Costumers">
                <form onSubmit={handleSubmit}>
                    <fieldset>
                        <legend>Info</legend>
                        <p>Cep:<input type="text" {...register("cep")} onChange={findCep} /></p>
                        <p>Street:<input type="text" {...register("street")} /></p>
                        <p>City:<input type="text" {...register("city")} /></p>
                        <p>Number:<input type="text" {...register("number")} /></p>
                    </fieldset>
                </form>
            </section>
        </>
    )
}

export default Costumers