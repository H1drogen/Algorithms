using DefaultNamespace;

namespace Program.Test.Easy;

[TestFixture]
public class ContainsDuplicateTests
{
    private ContainsDuplicate _containsDuplicate;

    [SetUp]
    public void Setup()
    {
        _containsDuplicate = new ContainsDuplicate();
    }

    [Test]
    public void Test1_DuplicateExists_ReturnsTrue()
    {
        int[] nums = {1, 2, 3, 1};
        bool result = _containsDuplicate.EfficientSolution(nums);
        Assert.IsTrue(result);
    }

    [Test]
    public void Test2_NoDuplicate_ReturnsFalse()
    {
        int[] nums = {1, 2, 3, 4};
        bool result = _containsDuplicate.EfficientSolution(nums);
        Assert.IsFalse(result);
    }
}
