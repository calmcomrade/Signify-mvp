import React, { useState, useEffect } from 'react';
import axios from 'axios';
import WebcamStreamCapture from './WebcamStreamCapture';
import MicRecorder from 'mic-recorder-to-mp3';
import SpeechRecognition, { useSpeechRecognition } from 'react-speech-recognition'
import logo from './logo.svg';
import settings from "./settings.svg";
import feedbackLogo from "./feedback.svg";
import translation from "./translation.svg";
import './App.css';


const App = () => {
  // State to manage the active section
  const [activeSection, setActiveSection] = useState('main');
  // Function to handle button click and switch sections
  const handleButtonClick = (section) => {
    if (section === 'feedback') {
      setSubmitted(false);
      setName('');
      setEmail('');
      setFeedback('');
    }
      setActiveSection(section);
  };
  const [texttranslate, setTextTranslate] = useState('');
  const [links, setLinks] = useState([{}]);
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [feedback, setFeedback] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [receivedText, setReceivedText] = useState('');

  const handleTextChange = (event) =>{
    setTextTranslate(event.target.value)
  }
  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handleFeedbackChange = (event) => {
    setFeedback(event.target.value);
  };

  const handleSubmit = () => {
    setSubmitted(true);
  };
  const [isRecording, setIsRecording] = useState(false);
  const [blobURL, setBlobURL] = useState(null);
  const [isBlocked, setIsBlocked] = useState(false);
  const [recorder, setRecorder] = useState(null);

  const {transcript, resetTranscript} = useSpeechRecognition ();

  function startRecording() {
    SpeechRecognition.startListening({continuous:true})
    console.log("listening")
  }

  function stopRecording(e) {
    e.preventDefault();
    setIsRecording(false);
    SpeechRecognition.stopListening()
  }
  const [videoUrls, setVideoUrls] = useState([]);
  const [currentVideoIndex, setCurrentVideoIndex] = useState(0);

  const handleSecondEnterClick = () => {
    axios.post('http://localhost:5000', { text: transcript })
      .then(response => {
        const receivedVideoUrls = response.data.received_text;
        setVideoUrls(receivedVideoUrls);
      })
      .catch(error => {
        console.error('Error fetching video URLs:', error);
      });
  };  

  const handleEnterClick = () => {
    axios.post('http://localhost:5000', { text: texttranslate })
      .then(response => {
        const receivedVideoUrls = response.data.received_text;
        setVideoUrls(receivedVideoUrls);
      })
      .catch(error => {
        console.error('Error fetching video URLs:', error);
      });
  };
  useEffect(() => {
    handleEnterClick();
  }, []);

  const handlePreviousVideo = () => {
    setCurrentVideoIndex(prevIndex => Math.max(prevIndex - 1, 0));
  };

  const handleNextVideo = () => {
    setCurrentVideoIndex(prevIndex => Math.min(prevIndex + 1, videoUrls.length - 1));
  };

  return (
    <div className="App">
      {/* Sidebar */}
      <nav>
        <ul>
          <li>
            <a href="#" className='logo'>
              <img src={logo} alt="logo" />
              <span className="nav-item">Signify</span>
            </a>
          </li>
          <li>
            <a href="#main" className={`other ${activeSection === 'main' ? 'active' : ''}`} onClick={() => handleButtonClick('main')}>
              <img src={translation} alt="translate" />
              <span className="nav-item"> Translate</span>
            </a>
          </li>
          <li>
            <a href="#feedback" className={`other ${activeSection === 'feedback' ? 'active' : ''}`} onClick={() => handleButtonClick('feedback')}>
              <img src={feedbackLogo} alt="feedback" />
              <span className="nav-item"> Feedback</span>
            </a>
          </li>
          <li>
            <a href="#" className={`other ${activeSection === 'settings' ? 'active' : ''}`} onClick={() => handleButtonClick('settings')}>
              <img src={settings} alt="settings" />
              <span className="nav-item"> Settings</span>
            </a>
          </li>
        </ul>
      </nav>

      {/* Main content */}
      <section id='main' style={{ display: activeSection === 'main' ? 'block' : 'none' }}>
        <div className='main-top'>
          <img src={translation} alt="translate" />
          <h1>Translate</h1>
          <div className='button-container'>
            {/* Buttons inside the 'Translate' section */}
            <button onClick={() => handleButtonClick('textToSign')}>Text/Audio to Sign</button>
            <button onClick={() => handleButtonClick('signToText')}>Sign to Text</button>
          </div>
          </div>
      </section>


      <section id='textToSign' style={{ display: activeSection === 'textToSign' ? 'block' : 'none' }}>
        <div className='signToText-top'>
            <img src={translation} alt="translate" />
            <h1>Translate Text to Sign</h1>
            <div className='Text to Sign'>
            </div>
            <div className='text'>
              <input placeholder='Enter text to translate' value={texttranslate} onChange={handleTextChange}></input>
              <button onClick={handleEnterClick}>Enter</button>
              <button onClick={startRecording} className='startrecord'>
            Start Recording
          </button>
          <button onClick={stopRecording} className='stoprecord'>
            Stop Recording
          </button>
          <textarea value={transcript} rows="2" cols="45"></textarea>
              <button className='enter' onClick={handleSecondEnterClick}>Enter</button>
              <button onClick={resetTranscript} className='enter'>Clear Text</button>
            </div>
            <div className='screen'>
                  <video
              src={videoUrls[currentVideoIndex]}
              autoPlay
              controls
              style={{ display: 'block' }}
            />
            <div>
              <button onClick={handlePreviousVideo} disabled={currentVideoIndex === 0}>Previous</button>
              <span>{videoUrls.length > 0 ? `${currentVideoIndex + 1}/${videoUrls.length}` : '0/0'}</span>
              <button onClick={handleNextVideo} disabled={currentVideoIndex === videoUrls.length - 1}>Next</button>
            </div>
                  </div>
            
            </div>
      </section>



      <section id='signToText' style={{ display: activeSection === 'signToText' ? 'block' : 'none' }}>
        <div className='signToText-top'>
          <img src={translation} alt="translate" />
          <h1>Translate Sign To Text</h1>
          <div className='signToText'>
          </div>
          <div className='screen'>  
          <WebcamStreamCapture />
          </div>
          </div>
      </section>



      {/* Feedback section */}
      <section id='feedback' style={{ display: activeSection === 'feedback' ? 'block' : 'none' }}>
      <div className='feedback-top'>
          <img src={feedbackLogo} alt="translate" />
          <h1>Feedback</h1>
          {submitted ? (
        <div className='submitted'>
          <p>Thank you for your feedback, {name}!</p>
        </div>
      ) : (
        <div className='feedback-box'>
          <label htmlFor="name" className='name'>  Name:</label>
          <input
            type="text"
            className='name-input'
            id="name"
            value={name}
            onChange={handleNameChange}
          />

          <br />

          <label htmlFor="email" className='email'>Email:</label>
          <input
            type="email"
            className='email-input'
            id="email"
            value={email}
            onChange={handleEmailChange}
          />

          <br />

          <label htmlFor="feedback" className='feedback-label'>Your Feedback:</label>
          <textarea
            id="feedback"
            className='feedback-input'
            rows="4"
            cols="50"
            value={feedback}
            onChange={handleFeedbackChange}
          ></textarea>

          <br />

          <button onClick={handleSubmit}>Submit Feedback</button>
        </div>
      )}
    </div>
      </section>


      {/* Settings section */}
      <section id='settings' style={{ display: activeSection === 'settings' ? 'block' : 'none' }}>
        {/* Add content for the Settings section here */}
        <h1>Settings Section</h1>
      </section>
    </div>
  );
};

export default App;
