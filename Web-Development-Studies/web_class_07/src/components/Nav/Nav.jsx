import { Link } from 'react-router-dom'

export default function Nav() {
    return (
        <header className='bg-slate-900 text-[#FFFFFF] p-4'>
            <nav className='flex justify-between items-center'>
                <h1 className='text-3xl font-extrabold'>Store</h1>
                <Link to='/' className='text-2xl hover:text-slate-300 transition-all duration-300'>Home</Link>
            </nav>
        </header>
    )
}
