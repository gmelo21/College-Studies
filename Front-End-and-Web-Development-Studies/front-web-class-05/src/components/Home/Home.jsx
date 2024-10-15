import Image from '../../assets/image.webp'

const Home = () => {
    return (
        <>
            <div className="flex flex-col h-48 justify-center items-center bg-slate-200 border-b border-slate-800 rounded-b-3xl">
                <h1 className="text font-bold text-8xl pb-7 underline text-center justify-center text-slate-800">Welcome!</h1>
                <button className="rounded-xl bg-slate-800 p-2 mt-1 text-white font-semibold animate-bounce transition-all duration-300 active:bg-slate-950 hover:bg-slate-900">Click here for nothing!</button>
            </div>
            <div className="flex flex-wrap justify-center mx-10">
                <div className="relative w-72 m-3 cursor-pointer border-2 shadow-lg rounded-b-xl items-center">
                    <div className="flex h-28 bg-slate-800 rounded-b-xl items-center justify-center">
                        <h1 className="absolute mx-auto text-center text-white font-bold text-6xl">My Post</h1>
                    </div>
                    <div className="p-2 border-b-2">
                        <h6>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Maiores at, repudiandae iste autem mollitia quis sunt provident minima optio voluptatum? Repudiandae exercitationem culpa sed? Reiciendis cum sit iste ullam quos.
                        </h6>
                    </div>
                </div>
                <div className="relative w-72 m-3 cursor-pointer border-2 shadow-lg rounded-b-xl items-center">
                    <div className="flex h-28 bg-slate-800 rounded-b-xl items-center justify-center">
                        <h1 className="absolute mx-auto text-center text-white font-bold text-6xl">My Post</h1>
                    </div>
                    <div className="p-2 border-b-2">
                        <h6>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Maiores at, repudiandae iste autem mollitia quis sunt provident minima optio voluptatum? Repudiandae exercitationem culpa sed? Reiciendis cum sit iste ullam quos.
                        </h6>
                    </div>
                </div>
                <div className="relative w-72 m-3 cursor-pointer border-2 shadow-lg rounded-b-xl items-center">
                    <div className="flex h-28 bg-slate-800 rounded-b-xl items-center justify-center">
                        <h1 className="absolute mx-auto text-center text-white font-bold text-6xl">My Post</h1>
                    </div>
                    <div className="p-2 border-b-2">
                        <h6>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Maiores at, repudiandae iste autem mollitia quis sunt provident minima optio voluptatum? Repudiandae exercitationem culpa sed? Reiciendis cum sit iste ullam quos.
                        </h6>
                    </div>
                </div>
            </div>
            <div className="h-28 transition-all duration-300 active:bg-slate-950 hover:bg-slate-900 cursor-pointer mb-2 py-8 px-8 max-w-sm mx-auto bg-slate-800 rounded-xl shadow-lg space-y-2 sm:py-4 sm:flex sm:items-center sm:space-y-0 sm:space-x-6">
                <img className="border-2 border-white block mx-auto h-24 rounded-full sm:mx-0" src={Image} alt="image" />
                <div className="text-center space-y-2 sm:text-left">
                    <div>
                        <p className='text-lg text-white font-bold'>
                            Melo
                        </p>
                        <p className="text-slate-300 font-medium">
                            Software Engineer
                        </p>
                        <p className="text-slate-400 font-medium pt-2 text-sm">
                            "Kept you waiting, huh?"
                        </p>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Home