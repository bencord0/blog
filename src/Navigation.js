import React, { Component } from "react";
import { Navbar, Nav, NavItem } from "react-bootstrap";
import { Link, withRouter } from "react-router-dom";

class Navigation_ extends Component {

  shouldComponentUpdate(nextProps, nextState) {
    const nextLocation = nextProps.location.pathname;
    const currentLocation = this.props.location.pathname;

    // no change
    if (nextLocation === currentLocation) {
      return false;
    }

    // render if and only if we are moving to the main pages
    return ["/", "/about/", "/archive/"].includes(nextLocation);
  }

  render() {
    console.log("Navigation: render");
    return (
      <Navbar fixedTop fluid>
        <Navbar.Header>
          <Navbar.Brand>
            <Link to="/">Fragments</Link>
          </Navbar.Brand>
          <Navbar.Toggle>
            <span className="icon-bar"/>
            <span className="icon-bar"/>
            <span className="icon-bar"/>
          </Navbar.Toggle>
        </Navbar.Header>
        <Navbar.Collapse>
          <Nav>
            <NavItem active onClick={() => this.props.history.push("/")}>Home</NavItem>
            <NavItem onClick={() => this.props.history.push("/about/")}>About</NavItem>
            <NavItem onClick={() => this.props.history.push("/archive/")}>Archive</NavItem>
          </Nav>
          <Navbar.Text>
            small, unrelated items. sometimes broken
          </Navbar.Text>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}

const Navigation = withRouter(Navigation_);
export default Navigation;

