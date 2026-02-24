from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', team=team)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team.name, 'Test Team')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30)
        self.assertEqual(activity.type, 'run')
        self.assertEqual(activity.duration, 30)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', team=team)
        workout = Workout.objects.create(user=user, description='Test Workout')
        self.assertEqual(workout.description, 'Test Workout')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)
