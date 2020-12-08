import React, { Component } from 'react';
//import './home.css';
import Grid from '@material-ui/core/Grid';
import { withStyles } from '@material-ui/core/styles';
//import Paper from '@material-ui/core/Paper';
import CodeSearch from '../components/CodeSearch';
import CodePrice from '../components/CodePrice';


const styles = {
    root: {
        flexGrow: 1,
    },
    paper: {
        height: 140,
        width: 200,
    },
    control: {
        padding: 2,
    },
  };
  
  class CodeInfo1 extends Component {
    constructor(props){
        super(props);
        this.state = {
            selectedCode:"",
        }
    }
    componentDidMount(){
  
    }
    componentDidUpdate(prevProps, prevState){
  
    }
    handleSelectedCode = (selectedCode)=>{
        console.log("CodeInfo handleSelectedCode", selectedCode);
        this.setState({selectedCode});
    }
    render(){
        return(
            <div>
                <span>
                    <CodeSearch code={this.state.selectedCode} handleSelectedCode={this.handleSelectedCode} />
                </span>
                <div>
                    <Grid>
                        <Grid container justify="center">
                            <Grid key={"codePrice"} item>
                                <CodePrice code={this.state.selectedCode}/>
                            </Grid>
                        </Grid>
                    </Grid>
                </div>
            </div>
        );
    }
  }
 /* const home = () => {
  
    return(
        <div>
            <h2>hello</h2>
        </div>
    )
}*/
  
  export default withStyles(styles)(CodeInfo1);