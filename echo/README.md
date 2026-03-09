# ECHO
An ambient sound layering platform to build, save, and share personalised soundscapes.

# Description
Echo is a full-stack ambient sound web application that lets users create immersive audio atmospheres by layering sounds together in a mixer and saving them as scenes.

The app allows users to upload, record, or link sounds from anywhere on the web, mix them together with individual volume controls, and save the result as a named scene. Scenes can be kept private or shared publicly for others to discover and play.

Echo was built out of a genuine love for ambient sound and the role it plays in focus, creativity, and relaxation. The goal was to create something that felt like a personal sound studio, intuitive, atmospheric, and genuinely useful.

# Deployment Link
Live App:

# Demo Login (for reviewers):
Username: admin
Password: 1234

# GitHub Repo
Link: https://github.com/SAGrika08/echo-app

# Timeframe & Working Team
Timeframe: 1 week
Team: Solo project

# Planning
Began by identifying the core user journey from adding a sound, to building a scene, to playing it back and worked outward from there.

Planning included:
* Writing user stories for sounds, scenes, and the mixer
* Building an ERD to model the relationships between users, sounds, and scenes
* Wireframing key pages:
    - Login and sign up
    - Sounds library
    - Mixer
    - Scene list
    - Scene detail
    - Public explore page
* Defining MVP scope and cutting non-essential features early
* Designing the data flow between sounds, scenes, and the SceneSound junction model

# Build Process
# Build Process
The project was built incrementally, starting with data modelling and base UI, followed by core feature development, and authentication added at the end.

The process included designing Django models and relationships first the Scene, Sound, and SceneSound junction model, then building out the base templates and consistent UI design system. From there, views and URL routing were implemented feature by feature, starting with sounds, then the mixer, then scenes. Once the core functionality was stable, authentication was added to protect user-owned data, followed by visual polish vinyl disc animations, gradient faders, and a consistent design language throughout.

Development focused on a clean separation between the mixer (create/edit) and the scene detail (read/play), giving each page a distinct purpose and feel.

# Technologies Used
Back End
- Python
- Django
- PostgreSQL
- Django ORM

Front End
- HTML
- CSS
- JavaScript 
- Lucide Icons
- Web Audio API

Other Tools & Practices
- Git & GitHub
- Django authentication and session management
- File uploads with Django's FileField
- Responsive design
- CSS animations and keyframes

# Key Highlights
* Custom mixer with real-time audio layering
Users can toggle sounds on and off, adjust individual volume levels with styled faders, and hear the mix playing live before saving.

* Vinyl disc aesthetic throughout
Every scene and sound is represented by an animated vinyl disc that spins on hover and during play, giving the app a strong visual identity.

* Flexible sound input
Sounds can be uploaded as files, linked via URL, or marked as recorded accommodating different workflows and demonstrating the app's flexibility.

* Public explore page
Scenes marked as public appear in a shared library accessible without logging in, turning Echo from a personal tool into a community platform.

* Edit scenes in the mixer
Existing scenes can be reopened in the mixer with all tracks and levels pre-loaded, allowing full non-destructive editing.

# Challenges
* Audio playback in the browser
Managing multiple simultaneous audio elements, ensuring only one scene plays at a time, and applying logarithmic volume curves required careful coordination between the DOM and the Web Audio API.

* Read-only vs interactive faders
The scene detail page displays faders in a read-only state that visually matches the interactive mixer faders, which required careful CSS separation between display and input logic.

* Designing a two-column mixer layout
Balancing the track list and save panel in a way that felt like a real mixer functional, clear, and atmospheric required several layout iterations.

# Wins
* End-to-end user journey
The app supports the complete flow from adding a sound, building a scene in the mixer, editing it later, playing it from the scene list or detail page, and discovering public scenes in the explore feed.

* Strong visual identity
The vinyl disc motif, gradient faders, and consistent typography give Echo a distinctive look that feels intentional rather than generic.

* Solo delivery of a full-stack app
Designing, building, and polishing every part of the app independently from the Django backend to the CSS animations within the project timeframe.

# Key Learnings / Takeaways
* Gained a deeper understanding of how Django's ORM handles many-to-many relationships through junction models and how to expose that data cleanly in templates.

* Learned how to manage browser audio with the Web Audio API including volume curves, simultaneous playback, and stopping audio on navigation.

* Understood the value of separating read and write views the scene detail and mixer serve very different purposes and keeping them distinct improved both UX and code clarity.

# Future Improvements
* Add a recording feature so users can capture audio directly in the browser without leaving the app
* Add search and filter to the sounds and scenes pages
* Add a heart/save feature on the explore page so users can bookmark public scenes to their own library
* Improve mobile layout especially for the mixer
* Add tags or categories to scenes for better discovery on the explore page