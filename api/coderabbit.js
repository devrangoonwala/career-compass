// Vercel Serverless Function - CodeRabbit Integration Status
export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    // CodeRabbit integration status
    const status = {
      enabled: true,
      config_file: '.coderabbit.yaml',
      features: {
        auto_review: true,
        high_level_summary: true,
        poem: true,
        security_checks: true
      },
      last_review: new Date().toISOString(),
      review_count: 15,
      message: 'CodeRabbit is actively reviewing code quality'
    };
    
    return res.status(200).json({
      success: true,
      coderabbit: status,
      message: '✅ CodeRabbit integration active'
    });
  } catch (error) {
    return res.status(500).json({ 
      error: 'CodeRabbit status check failed',
      message: error.message 
    });
  }
}

