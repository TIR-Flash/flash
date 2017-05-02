class YTVideo extends React.Component {
  render() {
    const opts = {
      height: '390',
      width: '640',
      playerVars: { 
        autoplay: 1
      }
    };

    return (
      <YouTube
        videoId="2g811Eo7K8U"
        opts={opts}
        onReady={this._onReady}
      />
    );
  }

  _onReady(event) {
    event.target.pauseVideo();
  }
}