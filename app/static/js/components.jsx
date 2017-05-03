import React from 'react';
import ReactDOM from 'react-dom';
import YouTube from 'react-youtube';

class YT extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      videoId: props.href.split("?")[1].split("v=")[1].split("&")[0],
    };
    this.onReady = this.onReady.bind(this);
  }

  onReady(event) {
    // console.log(`YouTube Player object for videoId: "${this.state.videoId}" has been saved to state.`);
  }

  render() {
    return (
      <div>
        <YouTube videoId={this.state.videoId} onReady={this.onReady}/>
      </div>
    );
  }
}

// ReactDOM.render(<YT href="https://www.youtube.com/watch?v=A71aqufiNtQ"/>, document.getElementById('video'));
$('#video').each(function(){
  console.log(this);
  ReactDOM.render(<YT href={$(this).attr('link')} />, this);
});