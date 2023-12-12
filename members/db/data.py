from members.models import Member

Member.objects.all()

member = Member(firstname='Emil', lastname='Refsnes')
member.save()

Member.objects.all().values()

member1 = Member(firstname='Tobias', lastname='Refsnes')
member2 = Member(firstname='Linus', lastname='Refsnes')
member3 = Member(firstname='Lene', lastname='Refsnes')
member4 = Member(firstname='Stale', lastname='Refsnes')
member5 = Member(firstname='Jane', lastname='Doe')
members_list = [member1, member2, member3, member4, member5]
for x in members_list:
    x.save()

Member.objects.all().values()