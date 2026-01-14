import ChatWidget from "./ChatWidget";

export default function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <h1>🏢 Secure Insurance Agency</h1>
        <p>Your trusted partner in comprehensive coverage</p>
      </header>

      <main className="app-main">
        <section className="hero">
          <h2>Welcome to Our Insurance Portal</h2>
          <p>
            We're here to help you with all your insurance needs. Have questions 
            about policies, claims, or coverage? Our AI assistant is ready to help!
          </p>
          <div className="cta-buttons">
            <button className="btn-primary">Get a Quote</button>
            <button className="btn-secondary">View Policies</button>
          </div>
        </section>

        <section className="features">
          <div className="feature-card">
            <div className="feature-icon">🛡️</div>
            <h3>Comprehensive Coverage</h3>
            <p>Protect what matters most with our tailored insurance solutions</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">⚡</div>
            <h3>Fast Claims Processing</h3>
            <p>File claims 24/7 and get responses within 24 hours</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">💬</div>
            <h3>Expert Support</h3>
            <p>Get instant answers from our AI assistant or speak with an agent</p>
          </div>
        </section>

        <section className="info-box">
          <h3>💡 Try Our AI Assistant</h3>
          <p>
            Click the chat button in the bottom-right corner to ask questions about:
          </p>
          <ul>
            <li>Filing claims and required documentation</li>
            <li>Understanding deductibles and coverage</li>
            <li>Adding drivers or updating policies</li>
            <li>Required documents for new policies</li>
          </ul>
        </section>
      </main>

      <ChatWidget />

      <style>{`
        * {
          margin: 0;
          padding: 0;
          box-sizing: border-box;
        }

        body {
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
            'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
            sans-serif;
          -webkit-font-smoothing: antialiased;
          -moz-osx-font-smoothing: grayscale;
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          min-height: 100vh;
        }

        .app-container {
          min-height: 100vh;
          padding-bottom: 40px;
        }

        .app-header {
          background: white;
          padding: 40px 20px;
          text-align: center;
          box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .app-header h1 {
          font-size: 32px;
          color: #2d3748;
          margin-bottom: 8px;
        }

        .app-header p {
          color: #718096;
          font-size: 16px;
        }

        .app-main {
          max-width: 1200px;
          margin: 40px auto;
          padding: 0 20px;
        }

        .hero {
          background: white;
          padding: 60px 40px;
          border-radius: 16px;
          text-align: center;
          box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
          margin-bottom: 40px;
        }

        .hero h2 {
          font-size: 36px;
          color: #2d3748;
          margin-bottom: 16px;
        }

        .hero p {
          font-size: 18px;
          color: #718096;
          line-height: 1.6;
          max-width: 700px;
          margin: 0 auto 32px;
        }

        .cta-buttons {
          display: flex;
          gap: 16px;
          justify-content: center;
          flex-wrap: wrap;
        }

        .btn-primary, .btn-secondary {
          padding: 14px 32px;
          border-radius: 12px;
          font-size: 16px;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.3s ease;
          border: none;
        }

        .btn-primary {
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          color: white;
          box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }

        .btn-primary:hover {
          transform: translateY(-2px);
          box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
        }

        .btn-secondary {
          background: white;
          color: #667eea;
          border: 2px solid #667eea;
        }

        .btn-secondary:hover {
          background: #f7fafc;
          transform: translateY(-2px);
        }

        .features {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
          gap: 24px;
          margin-bottom: 40px;
        }

        .feature-card {
          background: white;
          padding: 32px 24px;
          border-radius: 16px;
          text-align: center;
          box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
          transition: transform 0.3s ease;
        }

        .feature-card:hover {
          transform: translateY(-4px);
        }

        .feature-icon {
          font-size: 48px;
          margin-bottom: 16px;
        }

        .feature-card h3 {
          font-size: 20px;
          color: #2d3748;
          margin-bottom: 12px;
        }

        .feature-card p {
          color: #718096;
          line-height: 1.6;
        }

        .info-box {
          background: white;
          padding: 32px;
          border-radius: 16px;
          box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .info-box h3 {
          font-size: 24px;
          color: #2d3748;
          margin-bottom: 16px;
        }

        .info-box p {
          color: #718096;
          margin-bottom: 16px;
          font-size: 16px;
        }

        .info-box ul {
          list-style-position: inside;
          color: #718096;
          line-height: 1.8;
        }

        .info-box li {
          margin-bottom: 8px;
        }

        @media (max-width: 768px) {
          .hero h2 {
            font-size: 28px;
          }

          .hero p {
            font-size: 16px;
          }

          .features {
            grid-template-columns: 1fr;
          }
        }
      `}</style>
    </div>
  );
}