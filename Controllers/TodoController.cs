using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using TodoApp.Data;
using TodoApp.Models;

namespace TodoApp.Controllers;

public class TodoController : Controller
{
    private readonly ApplicationDbContext _context;

    public TodoController(ApplicationDbContext context)
    {
        _context = context;
    }

    // GET: Todo
    public async Task<IActionResult> Index()
    {
        var todoItems = await _context.TodoItems
            .OrderByDescending(t => t.CreatedDate)
            .ToListAsync();
        return View(todoItems);
    }

    // GET: Todo/Create
    public IActionResult Create()
    {
        return View();
    }

    // POST: Todo/Create
    [HttpPost]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Create([Bind("Title")] TodoItem todoItem)
    {
        if (ModelState.IsValid)
        {
            todoItem.CreatedDate = DateTime.Now;
            todoItem.IsCompleted = false;
            _context.Add(todoItem);
            await _context.SaveChangesAsync();
            return RedirectToAction(nameof(Index));
        }
        return View(todoItem);
    }

    // GET: Todo/Edit/5
    public async Task<IActionResult> Edit(int? id)
    {
        if (id == null)
        {
            return NotFound();
        }

        var todoItem = await _context.TodoItems.FindAsync(id);
        if (todoItem == null)
        {
            return NotFound();
        }
        return View(todoItem);
    }

    // POST: Todo/Edit/5
    [HttpPost]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> Edit(int id, [Bind("Id,Title,IsCompleted,CreatedDate")] TodoItem todoItem)
    {
        if (id != todoItem.Id)
        {
            return NotFound();
        }

        if (ModelState.IsValid)
        {
            try
            {
                _context.Update(todoItem);
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!TodoItemExists(todoItem.Id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }
            return RedirectToAction(nameof(Index));
        }
        return View(todoItem);
    }

    // POST: Todo/Delete/5
    [HttpPost, ActionName("Delete")]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> DeleteConfirmed(int id)
    {
        var todoItem = await _context.TodoItems.FindAsync(id);
        if (todoItem != null)
        {
            _context.TodoItems.Remove(todoItem);
            await _context.SaveChangesAsync();
        }
        return RedirectToAction(nameof(Index));
    }

    // POST: Todo/ToggleComplete/5
    [HttpPost]
    [ValidateAntiForgeryToken]
    public async Task<IActionResult> ToggleComplete(int id)
    {
        var todoItem = await _context.TodoItems.FindAsync(id);
        if (todoItem != null)
        {
            todoItem.IsCompleted = !todoItem.IsCompleted;
            await _context.SaveChangesAsync();
        }
        return RedirectToAction(nameof(Index));
    }

    private bool TodoItemExists(int id)
    {
        return _context.TodoItems.Any(e => e.Id == id);
    }
}
