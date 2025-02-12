import { Sidebar, Menu, MenuItem, SubMenu, sidebarClasses } from 'react-pro-sidebar'
import { Link } from 'react-router-dom'
import '../../base.css'

export default function Side() {
  return (
    <div className='sidebar'>
      <Sidebar
        rootStyles={{
          [`.${sidebarClasses.container}`]: {
            backgroundColor: '#E3E3E3', color: '#000000',
          }
        }}
      >
        <Menu>
          <SubMenu label='Dashboard'>
            <MenuItem component={<Link to='/' />}>Home</MenuItem>
            <MenuItem component={<Link to='/page1' />}>Page 1</MenuItem>
            <MenuItem component={<Link to='/page2' />}>Page 2</MenuItem>
            <MenuItem component={<Link to='/page3' />}>Page 3</MenuItem>
            <SubMenu label='Account'>
              <MenuItem>Login</MenuItem>
              <MenuItem>Logout</MenuItem>
            </SubMenu>
          </SubMenu>
        </Menu>
      </Sidebar>
    </div>
  )
}
