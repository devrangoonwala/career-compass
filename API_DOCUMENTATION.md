# API Documentation - Career Compass

The `api/` directory contains **Vercel Serverless Functions** that integrate all sponsor tools and make them accessible through the web interface.

## 🎯 Purpose

These API endpoints enable the frontend (`index.html`) to:
1. **Call sponsor tools** (Kestra, Oumi, CodeRabbit, Cline) from the browser
2. **Integrate all tools** to work together seamlessly
3. **Process data** and return results to the frontend
4. **Deploy on Vercel** as serverless functions

## 📁 API Endpoints

### 1. `/api/kestra.js` - Kestra Workflow Integration

**Purpose**: Executes the Kestra workflow (3 tasks) and returns results

**Method**: `POST`

**Request Body**:
```json
{
  "groq_api_key": "your-api-key"
}
```

**What it does**:
1. Fetches job data (Task 1)
2. Analyzes with Groq AI (Task 2)
3. Returns workflow results (Task 3)

**Response**:
```json
{
  "success": true,
  "kestra_tasks": {
    "task1_fetch": { "status": "success", "data": {...} },
    "task2_analyze": { "status": "success", "data": {...} },
    "task3_log": { "status": "success", "message": "..." }
  },
  "message": "✅ All 3 Kestra tasks completed successfully!"
}
```

**Used by**: Frontend when user uploads resume → triggers Kestra workflow

---

### 2. `/api/oumi.js` - Oumi Model Inference

**Purpose**: Analyzes job descriptions using the trained Oumi model

**Method**: `POST`

**Request Body**:
```json
{
  "job_description": "Senior Engineer $250k remote",
  "salary_info": "Salary information"
}
```

**What it does**:
- Analyzes job quality (good/bad/neutral)
- Extracts features (salary, remote work, experience level)
- Returns confidence scores

**Response**:
```json
{
  "success": true,
  "oumi_analysis": {
    "model": "SmolLM2-135M-Instruct (Oumi-trained)",
    "confidence": 0.92,
    "verdict": "good",
    "features": {
      "has_salary": true,
      "remote_work": true,
      "experience_level": "senior"
    }
  }
}
```

**Used by**: Frontend to analyze job quality and match candidates

---

### 3. `/api/coderabbit.js` - CodeRabbit Status

**Purpose**: Returns CodeRabbit integration status and code quality metrics

**Method**: `GET`

**What it does**:
- Checks CodeRabbit configuration
- Returns code quality status
- Shows review statistics

**Response**:
```json
{
  "success": true,
  "coderabbit": {
    "enabled": true,
    "config_file": ".coderabbit.yaml",
    "features": {
      "auto_review": true,
      "high_level_summary": true,
      "security_checks": true
    },
    "last_review": "2024-12-12T...",
    "review_count": 15
  }
}
```

**Used by**: Frontend to display CodeRabbit integration status

---

### 4. `/api/analyze.js` - Combined Analysis (All Tools)

**Purpose**: **Main integration endpoint** - Uses ALL sponsor tools together

**Method**: `POST`

**Request Body**:
```json
{
  "resume_text": "Resume content here...",
  "groq_api_key": "your-api-key"
}
```

**What it does**:
1. **CLINE**: Extracts skills from resume (AI-powered)
2. **OUMI**: Analyzes resume with trained model
3. **KESTRA**: Triggers workflow orchestration
4. **CODERABBIT**: Checks code quality status
5. **VERCEL**: Returns deployment info
6. **Generates**: Job matches based on all analyses

**Response**:
```json
{
  "success": true,
  "integration": {
    "cline": { "skills_extracted": 5, "status": "active" },
    "oumi": { "confidence": 0.89, "profile_quality": "high" },
    "kestra": { "workflow_id": "career_compass_logic", "status": "triggered" },
    "coderabbit": { "active": true, "code_quality": "excellent" },
    "vercel": { "deployed": true, "region": "iad1" }
  },
  "matches": [
    {
      "title": "Senior Software Engineer",
      "company": "Tech Solutions Inc.",
      "match": 95,
      "oumi_verified": true
    }
  ],
  "message": "✅ All 5 sponsor tools working together successfully!"
}
```

**Used by**: Frontend for complete resume analysis and job matching

---

## 🔄 How It Works Together

### User Flow:
1. User uploads resume → Frontend calls `/api/analyze`
2. `/api/analyze` orchestrates:
   - Calls `/api/oumi` for model analysis
   - Calls `/api/kestra` for workflow execution
   - Calls `/api/coderabbit` for status
   - Uses CLINE logic for skill extraction
3. Returns combined results → Frontend displays job matches

### Integration Flow:
```
Frontend (index.html)
    ↓
/api/analyze (Main orchestrator)
    ├──→ /api/oumi (Model analysis)
    ├──→ /api/kestra (Workflow execution)
    ├──→ /api/coderabbit (Status check)
    └──→ CLINE (Skill extraction)
    ↓
Combined Results → Frontend
```

## 🚀 Vercel Deployment

These are **Vercel Serverless Functions**:
- Automatically deployed when you run `npx vercel --prod`
- Each file in `api/` becomes an endpoint at `/api/[filename]`
- No server needed - runs on Vercel's edge network
- Scales automatically

## 💡 Why This Architecture?

1. **Separation of Concerns**: Each tool has its own endpoint
2. **Reusability**: Endpoints can be called independently
3. **Integration**: `/api/analyze` combines all tools
4. **Scalability**: Serverless functions scale automatically
5. **Frontend Integration**: Easy to call from browser JavaScript

## 📊 Summary

The `api/` directory is the **backend layer** that:
- ✅ Integrates all 5 sponsor tools (Cline, Kestra, Oumi, CodeRabbit, Vercel)
- ✅ Makes tools accessible from the web frontend
- ✅ Processes data and returns structured results
- ✅ Deploys as serverless functions on Vercel
- ✅ Enables real-time job matching and analysis

Without these APIs, the frontend couldn't interact with the sponsor tools. They're essential for the complete integration!

