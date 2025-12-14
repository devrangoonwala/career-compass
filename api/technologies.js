// Vercel Serverless Function - Technologies Status
export default async function handler(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    // Return all technologies with their status
    const technologies = {
      cline: {
        name: 'Cline',
        status: 'active',
        description: 'Autonomous coding workflows',
        color: 'blue'
      },
      kestra: {
        name: 'Kestra',
        status: 'active',
        description: 'Workflow orchestration with AI Agent',
        color: 'purple'
      },
      oumi: {
        name: 'Oumi',
        status: 'active',
        description: 'ML model training and inference',
        color: 'green'
      },
      coderabbit: {
        name: 'CodeRabbit',
        status: 'active',
        description: 'Automated code quality reviews',
        color: 'orange'
      },
      vercel: {
        name: 'Vercel',
        status: 'active',
        description: 'Serverless deployment platform',
        color: 'gray'
      }
    };
    
    return res.status(200).json({
      success: true,
      technologies: Object.values(technologies),
      message: 'All technologies active'
    });
  } catch (error) {
    return res.status(500).json({ 
      error: 'Failed to fetch technologies',
      message: error.message 
    });
  }
}

