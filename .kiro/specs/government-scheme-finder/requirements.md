# Requirements Document

## Introduction

SchemeSetu is a web-based application that helps Indian citizens discover government schemes they are eligible for based on their personal profile. The system uses AI to analyze user demographics and provide personalized scheme recommendations with detailed eligibility explanations in multiple Indian languages.

## Glossary

- **System**: The SchemeSetu web application
- **User**: Indian citizen seeking government scheme information
- **Scheme**: Government welfare program, subsidy, or benefit
- **Profile**: User's demographic and socioeconomic information
- **AI_Engine**: The generative AI component that analyzes eligibility
- **Eligibility_Criteria**: Specific requirements that determine scheme qualification

## Requirements

### Requirement 1: User Profile Collection

**User Story:** As a citizen, I want to input my personal details, so that the system can identify relevant schemes for my specific situation.

#### Acceptance Criteria

1. WHEN a user accesses the application, THE System SHALL display input fields for age, gender, state, occupation, income bracket, and social category
2. WHEN a user enters an age, THE System SHALL validate it is between 0 and 100 years
3. WHEN a user selects demographic options, THE System SHALL provide predefined choices for gender, state, occupation, income ranges, and social categories
4. THE System SHALL support major Indian states including Tamil Nadu, Karnataka, Maharashtra, Delhi, and Uttar Pradesh
5. THE System SHALL categorize users as General, OBC, SC/ST, or Minority

### Requirement 2: AI-Powered Scheme Analysis

**User Story:** As a citizen, I want the system to analyze my profile using AI, so that I receive accurate and personalized scheme recommendations.

#### Acceptance Criteria

1. WHEN a user submits their profile, THE AI_Engine SHALL identify exactly 3 government schemes the user is highly likely eligible for
2. WHEN analyzing eligibility, THE AI_Engine SHALL consider both central government and state-specific schemes
3. WHEN generating recommendations, THE AI_Engine SHALL prioritize schemes with the highest likelihood of user qualification
4. THE AI_Engine SHALL use the user's exact profile data to determine scheme matches
5. IF no API key is provided, THEN THE System SHALL display an error message and prevent analysis

### Requirement 3: Detailed Eligibility Explanation

**User Story:** As a citizen, I want to understand exactly why I qualify for each recommended scheme, so that I can confidently apply and gather the right documents.

#### Acceptance Criteria

1. FOR each recommended scheme, THE System SHALL provide the scheme name, one-line benefit summary, and detailed qualification reasoning
2. WHEN explaining qualification, THE System SHALL reference the user's specific age, gender, state, occupation, income, and category that match the scheme criteria
3. WHEN providing reasoning, THE System SHALL use the format "You qualify because you are [specific criteria from user profile]"
4. THE System SHALL list key documents needed for each recommended scheme
5. THE System SHALL provide a consolidated list of all required documents across recommended schemes

### Requirement 4: Multilingual Support

**User Story:** As a citizen who may not be fluent in English, I want to receive scheme information in my preferred Indian language, so that I can fully understand the recommendations.

#### Acceptance Criteria

1. THE System SHALL support output in English, Hindi, Tamil, Telugu, and Kannada languages
2. WHEN a user selects a language, THE System SHALL display all scheme recommendations and explanations in that language
3. THE System SHALL maintain the same level of detail and accuracy across all supported languages
4. THE System SHALL display language options in both English and native script
5. THE System SHALL use clear, simple language appropriate for common citizens

### Requirement 5: User Interface and Experience

**User Story:** As a citizen, I want an intuitive and accessible interface, so that I can easily navigate and use the application regardless of my technical expertise.

#### Acceptance Criteria

1. THE System SHALL display a clean, government-themed interface with Indian cultural elements
2. WHEN organizing input fields, THE System SHALL use a two-column layout for efficient space utilization
3. THE System SHALL provide a prominent search button to trigger scheme analysis
4. WHEN processing requests, THE System SHALL display a loading indicator with appropriate messaging
5. THE System SHALL show success confirmation when analysis is complete
6. THE System SHALL display error messages clearly when issues occur

### Requirement 6: API Integration and Configuration

**User Story:** As a user, I want to securely provide my API credentials, so that the system can access AI services while protecting my sensitive information.

#### Acceptance Criteria

1. THE System SHALL provide a sidebar configuration section for API key input
2. WHEN entering API keys, THE System SHALL mask the input for security
3. THE System SHALL validate API key presence before allowing scheme analysis
4. THE System SHALL configure the AI service with the provided credentials
5. IF API integration fails, THEN THE System SHALL display descriptive error messages

### Requirement 7: Response Formatting and Presentation

**User Story:** As a citizen, I want scheme information presented in a clear, structured format, so that I can easily understand and act on the recommendations.

#### Acceptance Criteria

1. THE System SHALL format AI responses with clear headings and bullet points
2. THE System SHALL separate different schemes with visual dividers
3. THE System SHALL highlight key information like scheme names and benefits
4. THE System SHALL present document requirements in an organized list format
5. THE System SHALL maintain consistent formatting across all supported languages