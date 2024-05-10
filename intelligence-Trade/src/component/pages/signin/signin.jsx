import React from "react";

// Image
import logo from "../../asset/img/logo.svg";
import { NavLink } from "react-router-dom";
const SignIn = () => {
  return (
    <>
      {/* <!-- page wrap --> */}
      <div className="section section--content">
        <div className="section__content">
          {/* <!-- form --> */}
          <form action="#" className="form form--content">
            <div className="form__logo-wrap">
              <NavLink to="/" className="form__logo">
                <img src={logo} alt="Loading" />
              </NavLink>

              <span className="form__tagline">
                Arbitrage trading <br />
                HTML Template
              </span>
            </div>

            <div className="form__group">
              <input type="text" className="form__input" placeholder="Email" />
            </div>

            <div className="form__group">
              <input
                type="password"
                className="form__input"
                placeholder="Password"
              />
            </div>

            <div className="form__group form__group--checkbox">
              <input id="remember" name="remember" type="checkbox" />
              <label for="remember">Remember Me</label>
            </div>

            <button className="form__btn" type="button">
              Sign in
            </button>

            <span className="form__delimiter">or</span>

            <div className="form__social">
              <a className="fb" href="#">
                <i className="ti ti-brand-facebook"></i>
              </a>
              <a className="tw" href="#">
                <i className="ti ti-brand-x"></i>
              </a>
              <a className="gl" href="#">
                <i className="ti ti-brand-google"></i>
              </a>
            </div>

            <span className="form__text form__text--center">
              Don't have an account? <NavLink to='/signUp'>Sign up!</NavLink>
              <br /> <NavLink to='/forgot'>Forgot password?</NavLink>
            </span>

            {/* <!-- design elements --> */}
            <span className="block-icon block-icon--purple">
				<NavLink to="/">
                    <i className="ti ti-login"></i>
                </NavLink>
            </span>
            <span className="screw screw--big-tr"></span>
            <span className="screw screw--big-bl"></span>
            <span className="screw screw--big-br"></span>
          </form>
          {/* <!-- end form --> */}
        </div>

        {/* <!-- animation background --> */}
        <div
          className="section__canvas section__canvas--full section__canvas--third gradient-background"
          id="canvas3"
        ></div>
      </div>
      {/* <!-- end page wrap --> */}
    </>
  );
};
export default SignIn;
