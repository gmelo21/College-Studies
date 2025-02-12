import Link from "next/link"

export default function Nav() {
  return (
    <div>
      <Link href="/account">Account</Link>
      <br></br>
      <Link href="/store">Store</Link>
      <br></br>
      <Link href="/">Home</Link>
      <br></br>
      <br></br>
    </div>
  )
}
