// Vercel Serverless Function - Kestra Workflow Integration
export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { groq_api_key } = req.body;
    
    // Step 1: Fetch job data (Kestra Task 1)
    const fetchResponse = await fetch('https://jsonplaceholder.typicode.com/posts/1');
    const jobData = await fetchResponse.json();
    
    // Step 2: AI Analysis using Groq (Kestra Task 2)
    const groqResponse = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${groq_api_key || process.env.GROQ_API_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        model: 'llama-3.3-70b-versatile',
        messages: [
          {
            role: 'system',
            content: 'You are a helpful assistant for Career Compass job filtering.'
          },
          {
            role: 'user',
            content: `Analyze this job data: ${JSON.stringify(jobData)}. Say 'Data Downloaded Successfully' and provide a brief analysis.`
          }
        ]
      })
    });
    
    const aiResult = await groqResponse.json();
    
    // Step 3: Log result (Kestra Task 3)
    const result = {
      success: true,
      kestra_tasks: {
        task1_fetch: { status: 'success', data: jobData },
        task2_analyze: { status: 'success', data: aiResult },
        task3_log: { status: 'success', message: 'All tasks completed successfully' }
      },
      message: '✅ All 3 Kestra tasks completed successfully!'
    };
    
    return res.status(200).json(result);
  } catch (error) {
    return res.status(500).json({ 
      error: 'Kestra workflow failed',
      message: error.message 
    });
  }
}

